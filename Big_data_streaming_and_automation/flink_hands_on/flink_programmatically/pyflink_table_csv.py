from pyflink.table import TableEnvironment, EnvironmentSettings, DataTypes,  CsvTableSource


FILE_PATH = "./fin_trxs.csv"
TABLE_NAME_TO_CREATE = "financial_trxs"

def main():
    print("Creating the enviornment")
    env_settings = EnvironmentSettings.new_instance()\
                                      .in_batch_mode()\
                                      .build()
    tbl_env = TableEnvironment.create(env_settings)
    print("environment is created")

    columns_names = ['trx_id', 'trx_date', 'src_curr', 'amnt_src_curr', 
                    'amnt_gbp', 'user_id', 'user_type', 'user_country']
    
    columns_types = [
        DataTypes.INT(),
        DataTypes.DATE(),
        DataTypes.STRING(),
        DataTypes.DOUBLE(),
        DataTypes.DOUBLE(),
        DataTypes.INT(),
        DataTypes.STRING(),
        DataTypes.STRING()
    ]

    source = CsvTableSource(
        FILE_PATH,
        columns_names,
        columns_types,
        ignore_first_line=False
    )

    tbl_env.register_table_source(TABLE_NAME_TO_CREATE, source)
    print(f"\nRegistered Tables List: {tbl_env.list_tables()}")

    tbl = tbl_env.from_path(TABLE_NAME_TO_CREATE)
    print(f"\nFinancial Trx schema is: {tbl.print_schema()}")

    print("\nfirst 10 rows are: ")
    tbl.limit(10).execute().print()


if __name__ == "__main__":
    main()
