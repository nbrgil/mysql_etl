"""Transformacoes no arquivo tax_applied_to_account (modelo 1)."""
import pandas as pd


class TaxAppliedToAccountTransf:
    """Contem as transformacoes para inserir na tabela fee."""

    def fix_float_values(self):
        """Arrumar colunas float."""
        self.df = self.df.fillna(0)
        self.df['percentual'] = \
            self.df['percentual'].str.replace(",", ".")
        self.df['fixed'] = \
            self.df['fixed'].str.replace(",", ".")

    def remove_invalid_fk(self, account_df):
        """Remove registro onde a conta eh invalida."""
        # TODO gerar um log quando essa situacao existe
        self.df = self.df[self.df['account_id'].isin(account_df['id'])]

    def rename_columns(self):
        """Renomear colunas para novo formato."""
        self.df.rename(columns={
            'payment_form_id': 'payment_method_id',
            'fixed': 'minimum_fee_value',
            'percentual': 'variable_fee_percentage'
        }, inplace=True)

    def set_constant_values(self):
        """Adicionar colunas com valores constantes."""
        self.df['antecipation_fee_percentage'] = 1.99
        self.df['antecipation_fee_interest_type'] = 'Compound'
        # TODO Multiplicar esse valor pela qtde na forma de pagamento
        self.df['installment_number'] = 1
        self.df['source_file'] = 'tax_applied_to_account.csv'

    def drop_columns(self):
        """Remove colunas nao utilizadas.

        Elas sao removidas apos tratamento em outra coluna
        """
        self.df.drop('id', axis=1, inplace=True)

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

    def transform(self, df, account_df, member_df):
        """Aplicar todas as transformacoes."""
        self.df = df
        self.fix_float_values()
        self.remove_invalid_fk(account_df)
        self.fill_join_values(member_df)
        self.set_constant_values()
        self.drop_columns()
        self.rename_columns()

        return self.df
