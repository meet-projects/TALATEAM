from __future__ import division

import sys

from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, MetaData, inspect, Table

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("ERROR: You need to give me a .db file. For example:")
        print("python print_database crudlab.db")
        sys.exit(1)

    db_file_name = sys.argv[1]

    engine = create_engine('sqlite:///%s' % db_file_name)

    metadata = MetaData(engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    table_names = inspect(engine).get_table_names()

    table_strings = []
    for table_name in table_names:
        table_string = '\n'
        table = Table(table_name, metadata, autoload=True)

        columns = [str(c).split('.')[-1] for c in table.columns]

        table_to_print = session.query(table).all()

        max_lengths = []

        for title, data in zip(columns, zip(*table_to_print)):
            max_lengths.append(max([len(repr(d)) for d in data]) + 2)
        row_format = ''.join(["{:>%d}" % length for length in max_lengths])

        # TODO this will break if the title name is too long OR the column
        # names are too short (unlikely but possible)
        header = row_format.format(*columns)
        width = len(header)
        title_pad = (width - len(table_name)) // 2

        table_string += (' ' * title_pad + table_name + ' ' * title_pad)
        hline = '\n' + '-' * len(header) + '\n'
        table_string += hline + header + hline

        row_strings = '\n'.join([row_format.format(*row) for row in table_to_print])

        table_string += row_strings

        table_strings.append(table_string)
    print('\n\n'.join(table_strings))

