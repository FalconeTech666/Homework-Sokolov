"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

a1 = 2.5
a2 = 2
a3 = "hello"
a4 = 1000.0001

float1 = type(a1) == float
float2 = type(a2) == float
float3 = type(a3) == float
float4 = type(a4) == float

all_floats = float1
if all_floats:
    all_floats = float2
if all_floats:
    all_floats = float3
if all_floats:
    all_floats = float4

print("Все дробные:", all_floats)

str1 = type(a1) == str
str2 = type(a2) == str
str3 = type(a3) == str
str4 = type(a4) == str

one_string = False
if str1:
    one_string = True
if not one_string and str2:
    one_string = True
if not one_string and str3:
    one_string = True
if not one_string and str4:
    one_string = True

print("Есть строка:", one_string)

int1 = type(a1) == int
int2 = type(a2) == int
int3 = type(a3) == int
int4 = type(a4) == int

pair_exists = False

if int1 and int3:
    pair_exists = True

if not pair_exists and int2 and int4:
    pair_exists = True

if not pair_exists and int3 and int4:
    pair_exists = True

print("Есть пара целочисленных:", pair_exists)