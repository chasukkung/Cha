def describe_pet(animal_type, pet_name):
    """반려동물에 관한 정보를 출력합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# 함수 호출은 함수 정의 바깥에서 이루어져야 합니다.
describe_pet('hamster', 'harry')
