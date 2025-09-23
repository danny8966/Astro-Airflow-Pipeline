'''
Task flow api allows us to use decorators instead of operators 
such as pythonOperator

Task 1 : To start with a number (say 100)
Task 2 : Ass 50 to the number
Task 3 : To multiply the result by 2
Task 4 : To divide the result by 10
'''

from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id='arithmetic_operator_tfapi'
) as dag:
    
    # Task 1 : To start with a number (say 100)
    @task
    def start_number():
        initial_value = 100
        print(f"starting_number: {initial_value}")
        return initial_value
    
    # Task 2 : Ass 50 to the number
    @task
    def add_fifty(number):
        new_value = number + 50
        print(f"Add fifty:{number}+50 = {new_value}")
        return new_value
    
    # Task 3 : To multiply the result by 2
    @task
    def multiply_two(number):
        new_value = number * 2
        print(f"Multiply by two:{number}*2= {new_value}")
        return new_value
        
    # Task 4 : To divide the result by 10
    @task 
    def divide_ten(number):
        new_value = number / 10
        print(f"Divide by ten: {number} / 10 = {new_value}")
        return new_value
    
    # dependencies
    start_value = start_number()
    second_value = add_fifty(start_value)
    third_value = multiply_two(second_value)
    fourth_value = divide_ten(third_value)
