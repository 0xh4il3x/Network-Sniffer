def get_filter():
    print("Select protocol to filter:")
    print("1. TCP")
    print("2. UDP")
    print("3. ICMP")
    print("4. All")
    choice = input("Enter your choice: ")

    if choice == '1':
        return "tcp"
    elif choice == '2':
        return "udp"
    elif choice == '3':
        return "icmp"
    else:
        return ""
