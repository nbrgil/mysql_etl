"""Transformacoes no arquivo fixed table fee."""
import pandas as pd


class FixedTableFeeTransf:
    """Contem as transformacoes para inserir na tabela fee."""

    def fix_float_values(self):
        """Arrumar colunas float."""
        self.df = self.df.fillna(0)
        self.df['fixed_tax_value'] = \
            self.df['fixed_tax_value'].str.replace(",", ".")
        self.df['parcel_tax_percentual'] = \
            self.df['parcel_tax_percentual'].str.replace(",", ".")

    def rename_columns(self):
        """Renomear colunas para novo formato."""
        self.df.rename(columns={
            'payment_form_id': 'payment_method_id',
            'fixed_tax_value': 'minimum_fee_value',
            'parcel_tax_percentual': 'variable_fee_percentage',
            'parcel_number': 'installment_number'
        }, inplace=True)

    def set_constant_values(self):
        """Adicionar colunas com valores constantes."""
        # TODO qual a regra para a taxa de antecipacao default?
        self.df['antecipation_fee_percentage'] = 1.99
        self.df['antecipation_fee_interest_type'] = 'Compound'
        self.df['source_file'] = 'fixed_table_fee.csv'

    def drop_columns(self):
        """Remove colunas nao utilizadas.

        Elas sao removidas apos tratamento em outra coluna
        """
        # TODO qual a necessidade real dessa coluna?
        self.df.drop('fixed_tax_percentual', axis=1, inplace=True)
        self.df.drop('id', axis=1, inplace=True)

    def df_crossjoin(self, df1, df2, **kwargs):
        """."""
        df1['_tmpkey'] = 1
        df2['_tmpkey'] = 1

        res = pd.merge(df1, df2, on='_tmpkey', **kwargs). \
            drop('_tmpkey', axis=1)
        res.index = pd.MultiIndex.from_product((df1.index, df2.index))

        df1.drop('_tmpkey', axis=1, inplace=True)
        df2.drop('_tmpkey', axis=1, inplace=True)

        return res

    def generate_default_df(self, current_fee_df, account_df):
        """."""
        crossed_acc_df = self.df_crossjoin(
            account_df.query('fee_type in (1,3)'), self.df
        )
        default_df = crossed_acc_df.merge(
            current_fee_df,
            left_on=['id', 'payment_method_id', 'installment_number'],
            right_on=['account_id', 'payment_method_id', 'installment_number'],
            how='left', indicator='merge_column', suffixes=('', '_y')
        )

        default_df = (default_df[default_df.merge_column == 'left_only'])

        self.df = default_df.loc[:, [
            'id', 'payment_method_id', 'installment_number',
            'minimum_fee_value', 'variable_fee_percentage',
            'antecipation_fee_percentage', 'antecipation_fee_interest_type',
            'source_file'
        ]]

        self.df.rename(columns={
            'id': 'account_id'
        }, inplace=True)

    def fill_join_values(self, member_df):
        """Preencher member_id usando como base account_id."""
        # TODO tentar usar left join para nao perder registros sem membro
        self.df = self.df.merge(
            member_df[['id']], left_on='account_id',
            right_on='id', how='inner'
        )
        self.df.rename(columns={
            'id': 'member_id'
        }, inplace=True)

    def remove_channel_value(self, account_df, account_channel_df):
        """Remove registros onde o canal tem prioridade."""
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

    def transform(
        self, df, current_fee_df, account_df, member_df, account_channel_df
    ):
        """Aplicar todas as transformacoes."""
        self.df = df
        self.fix_float_values()
        self.set_constant_values()
        self.drop_columns()
        self.rename_columns()
        self.generate_default_df(current_fee_df, account_df)
        self.fill_join_values(member_df)
        self.remove_channel_value(account_df, account_channel_df)

        return self.df
