begin = 0
end = 100

for number in range (begin, end + 1):
    match number:
        case jibjab if number % 15 == 0:
            print("jibjab")
        case jib if number % 3 == 0:
            print("jib")
        case jab if number % 5 == 0:
            print("jab")
        case default:
            print(number)