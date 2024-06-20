import os
import pandas as pd
from cx_Oracle import makedsn, connect


def connection():
    dsn_tns = makedsn(os.environ.get("DB_HOSTNAME"), os.environ.get("DB_PORT"),
                      service_name=os.environ.get("DB_SERVICE_NAME"))
    conn = connect(user=os.environ.get("DB_USER"), password=os.environ.get("DB_PASSWORD"), dsn=dsn_tns)
    print("Successful connection to database")
    return conn


def from_db_to_csv(conn, process_name):
    cursor = conn.cursor()

    cursor.execute('''
    select * from some_table
''')

    column_names = [desc[0] for desc in cursor.description]

    # Initialize variables for chunk processing
    chunk_size = 200000  # Adjust the chunk size based on your memory constraints
    sheet_number = 1
    excel_file_name = f"{process_name}.xlsx"

    writer = pd.ExcelWriter(excel_file_name, engine='xlsxwriter')

    csv_file_name = f"{process_name}.csv"
    header_written = False

    with open(csv_file_name, 'w', encoding='cp1251', newline='') as f:
        while True:
            data = cursor.fetchmany(chunk_size)
            if not data:
                break
            chunk_df = pd.DataFrame(data, columns=column_names)

            date_columns = ["DATE_OF_CHARGE"]
            for column in date_columns:
                if column in chunk_df.columns:
                    chunk_df[column] = pd.to_datetime(chunk_df[column], errors='coerce').dt.strftime('%d/%m/%Y')

            sheet_name = f'Sheet{sheet_number}'
            chunk_df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Apply date formatting
            workbook = writer.book
            worksheet = writer.sheets[sheet_name]
            date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})

            for column in date_columns:
                if column in chunk_df.columns:
                    col_idx = chunk_df.columns.get_loc(column)
                    worksheet.set_column(col_idx, col_idx, 12, date_format)

            # Save the chunk to the Excel file
            writer.close()

            # Read the chunk back from the Excel file and write to CSV
            sheet_df = pd.read_excel(excel_file_name, sheet_name=sheet_name)
            if not header_written:
                sheet_df.to_csv(f, sep=';', encoding='cp1251', index=False, header=True)
                header_written = True
            else:
                sheet_df.to_csv(f, sep=';', encoding='cp1251', index=False, header=False, mode='a')

    cursor.close()

    return csv_file_name
