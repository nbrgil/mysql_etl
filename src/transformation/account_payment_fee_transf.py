"""Transformacoes no arquivo account_payment_fee (modelo 2)."""


class AccountPaymentFee:
    """."""

    def rename_columns(self):
        """Renomear colunas para novo formato."""
        self.df.rename(columns={
            'payment_form_id': 'payment_method_id',
            'fixed': 'minimum_fee_value',
            'parcel_tax_percentual': 'variable_fee_percentage',
            'antecipation_percentage': 'antecipation_fee_percentage'
        }, inplace=True)

    def set_constant_values(self):
        """Adicionar colunas com valores constantes."""
        self.df['antecipation_fee_percentage'] = 2.89
        self.df['antecipation_fee_interest_type'] = 'Simple'

    def drop_columns(self):
        """."""
        self.df.drop('fixed_tax_percentual', axis=1, inplace=True)

    def remove_invalid_fk(self, account_df, payment_form_df):
        """."""
        self.df = self.df[self.df['account_id'].isin(account_df['id'])]

    def fill_join_values(self, member_df):
        """."""
        self.df = self.df.merge(
            member_df[['id']], left_on='account_id',
            right_on='id', how='left'
        )
        self.df.rename(columns={
            'id_x': 'id',
            'id_y': 'member_id'
        }, inplace=True)

    def transform(self, df, account_df, payment_form_df, member_df):
        """."""
        self.df = df
        self.rename_columns()
        self.set_constant_values()
        self.drop_columns()
        self.remove_invalid_fk(account_df, payment_form_df)
        self.fill_join_values(member_df)

        return self.df
