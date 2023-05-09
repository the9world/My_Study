age=19
money=20000
chicken=20000
beer=10000
drink=5000

# if money>= chicken:
#     money = money-chicken
#     print("chicken만 먹는다")
# if money>=beer and age >=20:
#     money = money-beer
#     print("beer도 먹는다")
# if money>= drink:
#     money = money-drink
#     print("drink도 먹는다")

# if money>= chicken+beer+drink and age >= 20:
#     print("chicken, beer, drink 먹는다")
# elif money>= chicken+beer and age >=20:
#     print("chicken과 beer를 먹는다")
# elif money>= chicken + drink:
#     print("chicken과 drink를 먹는다")
# elif money>= chicken:
#     print("chickne만 먹는다")
# elif money>= beer+drink and age >20:
#     print("beer와 drink를 먹는다")
# elif money>= beer and age>= 20:
#     print("beer를 먹는다")
# elif money>= drink:
#     print("drink를 마신다")


if money>= chicken:
    print("chicken을 먹는다")
    if money-chicken >= beer and age>=20 :
        print("beer를 먹는다")    
        if money-chicken -beer >= drink:
             print("drink를 먹는다")
    if money - chicken >=drink:
        print("drink를 먹는다")
elif money>= beer and age >=20:
    print("drink도 먹는다")
    if money - beer>= drink:
        print("음료수를 먹는다")
elif money >= drink:
    print("음료수를 먹는다")