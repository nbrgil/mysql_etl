"""."""


class ChannelFixedFeeTransf:
    """Contem as transformacoes para inserir na tabela fee."""

    def set_account_id(self, account_channel_df, account_df):
        """Preencher account id usando a tabela de canais."""
        account_channel_df = account_channel_df.merge(
            account_df[['id', 'negotiated_tax']], left_on='account_id',
            right_on='id', how='inner'
        )

        self.df = self.df.merge(
            account_channel_df[account_channel_df.negotiated_tax == 0],
            left_on='channel_id',
            right_on='channel_id', how='inner'
        )
        self.df.drop('negotiated_tax', axis=1, inplace=True)
        self.df.drop('channel_id', axis=1, inplace=True)

    def set_member_id(self, member_df):
        """Preencher member_id usando como base account_id."""
        self.df = self.df.merge(
            member_df[['id']], left_on='account_id',
            right_on='id', how='inner', suffixes=('', '_merge')
        )
        self.df.drop('id_merge', axis=1, inplace=True)
        self.df.rename(columns={
            'id': 'member_id'
        }, inplace=True)

    def rename_columns(self):
        """Renomear colunas para novo formato."""
        self.df.rename(columns={
            'payment_form_id': 'payment_method_id',
            'parcel_number': 'installment_number',
            'fixed_tax_value': 'minimum_fee_value',
            'parcel_tax_percentual': 'variable_fee_percentage'
        }, inplace=True)

    def drop_columns(self):
        """Remove as colunas nao usada."""
        # TODO qual a necessidade real dessa coluna?
        self.df.drop('fixed_tax_percentual', axis=1, inplace=True)

    def set_constant_values(self):
        """Adicionar colunas com valores constantes."""
        # TODO qual a regra para a taxa de antecipacao por canal?
        self.df['antecipation_fee_percentage'] = 1.99
        self.df['antecipation_fee_interest_type'] = 'Compound'
        self.df['source_file'] = 'channel_fixed_fee.csv'

    def transform(
        self, df, account_df, account_channel_df, channel_df, member_df
    ):
        """Aplicar todas as transformacoes."""
        self.df = df
        self.set_account_id(account_channel_df, account_df)
        self.set_member_id(member_df)
        self.rename_columns()
        self.drop_columns()
        self.set_constant_values()

        return self.df
