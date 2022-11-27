from utils import process_item

if __name__ == '__main__':
    is_running = True
    while is_running:
        x = input("Enter a number (Or enter 'q' to stop): ")
        if x == 'q':
            is_running = False
        elif not x.isnumeric():
            print("Please enter a valid number!")
        else:
            print(process_item(int(x)))
