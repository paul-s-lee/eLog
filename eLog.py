def main():

    while True:
        

        print('eLog \t\t\t\t\t ver: 0.0.1')
        print('-----------------------------------------------------')
        print('E - Enter expenditure')
        print('D - Display Expenditures')
        print('R - Remove Expenditures')
        choice = input('Enter choice: ')
        print('')

        if choice == 'e':

            name = input('Enter product or service name: ')
            price = input('Enter product or service price: ')
            date = input('Enter product or service date of purchase: ')

            f = open('expenditures.txt', 'a+')
            f.write(date + ' ')
            f.write(name + ' ')
            f.write(price + ' ')
            f.write('\n')
            f.close()

        elif choice == 'd':

            f = open('expenditures.txt', 'r')
            expenditures = f.readlines()
            f.close()

            index = 0
            
            for line in expenditures:
                print('item', index,': ', line.strip('\n')) # .strip() gets rid of the newline that is read into the expenditures[] list
                index = index + 1

        elif choice == 'r':

            index = int(input('Enter index to remove item: '))

            f = open('expenditures.txt', 'r')
            expenditures = f.readlines()
            f.close()

            del expenditures[index]

            f = open('expenditures.txt', 'w')
            for line in expenditures:

                f.write(line)

            f = open('expenditures.txt', 'r')
            expenditures2 = f.readlines()
            f.close()

            print('Success!')

        elif choice == 'l':

            f = open('expenditures.txt', 'r')
            expenditures = f.readlines()
            f.close()

            

            

        print('')

main()

