def create_item():
    while True:
        name=input('Enter the task name:\t')
        if name.strip()=="" or len(name.strip())<5:
            print('='*80)    
            print('Invalid input')
            continue
        else:
            break

    content=input('Enter the task Content:\t')
       
    
        