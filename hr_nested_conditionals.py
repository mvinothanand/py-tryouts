# return date and due date are provided. calculate the fine
# if returned within the due date - no fine
# if returned within the calendar month as the due date, 
#   15 hackos * overdue days
# if returned with in the same calendar year as the due date,
#   500 hackos * overdue days
# if beyond the calendar year, fixed fine of 10000 hackos

from datetime import datetime

def main():
    #return_day, return_month, return_year = input().strip().split(' ')
    return_day, return_month, return_year = '8 4 12'.strip().split(' ')
    if int(return_year) < 2000:
        return_year = str(2000 + int(return_year))

    #due_day, due_month, due_year = input().strip().split(' ')
    due_day, due_month, due_year = '1 1 1'.strip().split(' ')
    if int(due_year) < 2000:
        due_year = str(2000 + int(due_year))

    return_date = datetime.strptime(f'{return_day}-{return_month}-{return_year}', '%d-%m-%Y')

    print(f'Return date: {return_date}')
    due_date = datetime.strptime(f'{due_day}-{due_month}-{due_year}', '%d-%m-%Y')
    print(f'Due date: {due_date}')

    #print(type((return_date - due_date).days))
    diff = (return_date - due_date).days
    diff_in_months = int(diff/30)
    print(f'due for {diff} days')
    print(f'due for {diff_in_months} months')
    if diff <= 0:
        fine = 0
    else:
        if return_year == due_year and return_month == due_month:
            fine = 15 * diff
        elif return_year == due_year:
            fine = 500 * diff_in_months
        else:
            fine = 10000

    print(f'fine is: {fine}')


if __name__ == '__main__':
    main()