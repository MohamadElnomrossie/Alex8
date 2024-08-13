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
    task=name+","+content+","+'open'+"\n"
    
    with open('data.txt','a') as t:
        t.write(task)
        
def view_all_tasks():
    tasks=[]
    task_dict={}
    with open('data.txt','r') as t:
        tasks=t.readlines()
        
    for idx,task in enumerate(tasks):
        task_details=task.strip().split(",")
        
        task_dict[idx+1]=task
        
        task_name=task_details[0]
        task_content=task_details[1]
        task_status=task_details[2]
        print(idx+1,f"Name: {task_name}")
        print(f"Content: {task_content}")
#         print(f"Status: {task_status}")
        print("="*60)
    return task_dict

def delete_task(task):
    tasks=""
    with open ('data.txt', 'r') as t:
        text=t.read()
    text=text.replace(task,"")
    with open ('data.txt', 'w') as t:
        t.write(text)
    print("Deleted")
    
        