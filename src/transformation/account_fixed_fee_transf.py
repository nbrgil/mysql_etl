"""Transformacoes no arquivo account_fixed_table_fee (modelo 3)."""


class AccountFixedFeeTransf:
    """Contem as transformacoes para inserir na tabela fee."""

    def rename_columns(self):
        """Renomear colunas para novo formato."""
        self.df.rename(columns={
            'payment_form_id': 'payment_method_id',
            'parcel_number': 'installment_number',
            'fixed_tax_value': 'minimum_fee_value',
            'parcel_tax_percentual': 'variable_fee_percentage'
        }, inplace=True)

    def set_constant_values(self):
        """Adicionar colunas com valores constantes."""
        self.df['antecipation_fee_percentage'] = 2.89
        self.df['antecipation_fee_interest_type'] = 'Simple'
        self.df['source_file'] = 'account_fixed_table_fee.csv'

    def drop_columns(self):
        """Remove a coluna nao usada."""
        # TODO qual a necessidade real dessa coluna?
        self.df.drop('fixed_tax_percentual', axis=1, inplace=True)
        self.df.drop('id', axis=1, inplace=True)

    def remove_invalid_fk(self, account_df):
        """Remove registro onde a conta eh invalida."""
        # TODO gerar um log quando essa situacao existe
        self.df = self.df[self.df['account_id'].isin(account_df['id'])]

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

    def fill_join_values(self, member_df):
        """Preencher member_id usando como base account_id."""
        self.df = self.df.merge(
            member_df[['id']], left_on='account_id',
            right_on='id', how='left'
        )
        self.df.rename(columns={
            'id': 'member_id'
        }, inplace=True)

    def transform(self, df, account_df, member_df, account_channel_df):
        """Aplicar todas as transformacoes."""
        self.df = df
        self.rename_columns()
        self.set_constant_values()
        self.drop_columns()
        self.remove_invalid_fk(account_df)
        self.fill_join_values(member_df)
        self.remove_channel_value(account_df, account_channel_df)

        return self.df
