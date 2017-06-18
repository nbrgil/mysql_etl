"""Transformacoes no arquivo account_payment_fee (modelo 2)."""
import pandas as pd


class AccountPaymentFeeTransf:
    """Contem as transformacoes para inserir na tabela fee."""

    def fix_float_values(self):
        """Arrumar colunas float."""
        self.df = self.df.fillna(0)
        self.df['one_parcel'] = \
            self.df['one_parcel'].str.replace(",", ".")
        self.df['between_two_and_six_parcels'] = \
            self.df['between_two_and_six_parcels'].str.replace(",", ".")
        self.df['antecipation_percentage'] = \
            self.df['antecipation_percentage'].str.replace(",", ".")
        self.df['fixed'] = \
            self.df['fixed'].str.replace(",", ".")

    def rename_columns(self):
        """Renomear colunas para novo formato."""
        self.df.rename(columns={
            'payment_form_id': 'payment_method_id',
            'parcel_number': 'installment_number',
            'fixed': 'minimum_fee_value',
            'parcel_tax_percentual': 'variable_fee_percentage',
            'antecipation_percentage': 'antecipation_fee_percentage',
            'one_parcel': '1'
        }, inplace=True)

    def set_constant_values(self):
        """Adicionar colunas com valores constantes."""
        self.df['antecipation_fee_interest_type'] = 'Simple'
        self.df['source_file'] = 'account_payment_fee.csv'

    def drop_columns(self):
        """Remove colunas nao utilizadas."""
        self.df.drop('between_two_and_six_parcels', axis=1, inplace=True)
        self.df.drop('more_than_seven_parcels', axis=1, inplace=True)
        self.df.drop('id', axis=1, inplace=True)

    def create_installment_columns(self):
        """Duplica colunas com valor (ver pivot_installment_values)."""
        for x in range(2, 7):
            self.df[str(x)] = self.df['between_two_and_six_parcels']
        for x in range(7, 13):
            self.df[str(x)] = self.df['more_than_seven_parcels']

    def pivot_installment_values(self):
        """Efetua um pivot das colunas de valores.

        Esse arquivo nao possui informacao para cada mes. Por isso, os
        registros serao duplicados para facilitar a consulta.
        """
        self.df = pd.melt(self.df, id_vars=[
            'account_id', 'payment_method_id', 'minimum_fee_value',
            'antecipation_fee_percentage', 'antecipation_fee_interest_type',
            'member_id', 'source_file'
        ], value_vars=[
            # TODO Deixar o numero de parcelas dinamico
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'
        ], var_name='installment_number', value_name='variable_fee_percentage')

    def remove_invalid_account(self, account_df):
        """Remove registro onde a conta eh invalida."""
        # TODO gerar um log quando essa situacao existe
        self.df = self.df[self.df['account_id'].isin(account_df['id'])]

    def fill_join_values(self, member_df):
        """Preenche member_id usando como base account_id."""
        self.df = self.df.merge(
            member_df[['id']], left_on='account_id',
            right_on='id', how='left'
        )

        self.df.rename(columns={
            'id_x': 'id',
            'id_y': 'member_id'
        }, inplace=True)

    def remove_channel_value(self, account_df, account_channel_df):
        """Remove registros onde o canal tem prioridade.

        Eh realizado um merge com a lista de contas de um canal, somente
        considerando as contas que nao foram negociadas. As linhas com essas
        contas sao retiradas, pois serao inseridas com o valor do canal
        posteriormente
        """
        account_not_negotiated = account_df[account_df.negotiated_tax == 0]

        account_with_channel = account_not_negotiated.merge(
            account_channel_df, left_on='id',
            right_on='account_id', how='inner'
        )

        self.df = self.df.merge(
            account_with_channel[['id']], left_on='account_id',
            right_on='id', indicator='merge_column', how='left',
            suffixes=('', '_y')
        )
        self.df = (self.df[self.df.merge_column == 'left_only'])
        self.df.drop('id', axis=1, inplace=True)
        self.df.drop('merge_column', axis=1, inplace=True)

    def transform(self, df, account_df, member_df, account_channel_df):
        """Aplicar todas as transformacoes."""
        self.df = df
        self.fix_float_values()
        self.remove_invalid_account(account_df)
        self.fill_join_values(member_df)
        self.set_constant_values()

        self.create_installment_columns()
        self.drop_columns()
        self.rename_columns()
        self.pivot_installment_values()
        self.remove_channel_value(account_df, account_channel_df)

        return self.df
