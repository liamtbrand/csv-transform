import csv

def transform(
        source_csv_file_path,
        target_csv_file_path,
        column_mapping
    ):

    with open(source_csv_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        with open(target_csv_file_path, 'w') as outfile:
            csvwriter = csv.writer(outfile, delimiter=',')

            # Fetch the columns and map them. Write output columns.
            columns = csvreader.__next__()
            csvwriter.writerow([m[0] for m in column_mapping])

            for row in csvreader:
                kwargs = {columns[i]:row[i] for i in range(0, len(row))}
                csvwriter.writerow([m[1](**kwargs) for m in column_mapping])
