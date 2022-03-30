
import csv


def read_dict_anh_viet():

    table_data = [[]]  # ALL row data
    row_data = ['', '', '']  # One row data
    tu_dich = ''  # Chua dau '@'
    phat_am = ''  # Chua dau '//'
    mo_ta = ''    # Chua dau '*, °, ◦, !, +'

    # Using readlines()
    file1 = open('ngaanh.dict', 'r', encoding="utf8")
    Lines = file1.readlines()

    count = 0
    for line in Lines:
        count += 1

        # line = line.replace("\n", "")

        if line.__contains__("@"):
            line = line.replace("\n", "")
            if (count != 1):
                row_data[2] = mo_ta
                table_data.append(row_data)

                # reset
                mo_ta = ''
                row_data = ['', '', '']

            #######
            print(line)
            tu_dich = line
            row_data[0] = tu_dich



        if line[0].__eq__("/"):
            line = line.replace("\n", "")
            phat_am = line
            row_data[1] = phat_am

        if line.__contains__("°") or line.__contains__("◦") or line.__contains__("*") or line.__contains__("!") or line.__contains__("+"):
            line = line.replace("\n", " .xuoc_n. ")
            mo_ta += line


        if count== len(Lines):
            row_data[2] = mo_ta
            table_data.append(row_data)


    # print(table_data)
    return table_data


def read_dict_anh_anh():
    table_data = [[]]  # ALL row data
    row_data = ['', '', '']  # One row data
    tu_dich = ''  # Chua dau '@'
    phat_am = ''  # Chua dau '//'
    mo_ta = ''    # Chua dau '*, °, ◦, !, +'

    # Using readlines()
    file1 = open('ngaviet.dict', 'r', encoding="utf8")
    Lines = file1.readlines()

    count = 0
    for line in Lines:
        count += 1

        if line.__contains__("@"):
            line = line.replace("\n", "")
            if (count != 1):
                row_data[2] = mo_ta
                table_data.append(row_data)

                # reset
                mo_ta = ''
                row_data = ['', '', '']

            #######
            print(line)
            tu_dich = line
            row_data[0] = tu_dich

            continue

        if line[0].__eq__("/"):
            line = line.replace("\n", "")
            phat_am = line
            row_data[1] = phat_am
            continue

        if line.__contains__("°") or line.__contains__("◦") or line.__contains__("*") or line.__contains__("!") or line.__contains__("+"):
            line = line.replace("\n", " .xuoc_n. ")
            mo_ta += line
            continue

        line = line.replace("\n", " .xuoc_n. ")
        mo_ta += line

        if count >= len(Lines):
            row_data[2] = mo_ta
            table_data.append(row_data)

    return table_data


def write_csv(data):
    with open('ngaanh.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        header = ['Russian', 'Pronounce', 'English']
        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)


# def read_csv(data):





if __name__ == '__main__':
    data = read_dict_anh_viet()

    write_csv(data)



