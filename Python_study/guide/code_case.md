## 프로그래밍 코드 표기법
### 헝가리안 표기법 (Hungarian Notation)
1.  변수 선언 시 변수의 의미를 명확하게 파악할 수 있도록  
접두어를 붙이는 표기법
2. 변수명 단어의 시작에 접두어를 붙여서 해당 변수가  
무슨 타입의 변수인지 명확하게 알기 위해 사용
   - int nCount; short sLevel; long lHp;  
     단어 시작에 해당 타입을 나타내는 접두어를 붙여 표기

### 카멜 표기법 (Camel Case)
1. 낙타의 혹처럼 들쑥날쑥한 모양으로 구분한다해서  
카멜(낙타 camel) 표기법이다.
   - 단어와 단어 사이를 점이나 공백 없이 대소문자로 구분하여 표현하는 방식이다.
   - 소문자로 시작한다.
   - 자바스크립트, C# 등의 언어들은 카멜 표기법을 권장하고 있다.
2. 언더바( _ )를 사용하면 가독성이 떨어져서  
대소문자로 구분하여 가독성을 높이기 위해 사용한다.  
(사람마다 가독성의 기준이 다르다,  
모두가 언더바는 가독성이 떨어진다 단정할 수는 없는 부분)
   - private int camleValueTest;  
변수 명 시작은 소문자, 그 뒤 단어들의 시작은 대문자

### 파스칼 표기법 (Pascal Case)
1. 단어의 첫 문자를 대문자로 표기하여  
단어와 단어사이를 구분하는 표기법
    - namespace, event, property, class 명 지정에 주로 사용
2. 카멜(camel) 표기법과 마찬가지로 가독성을 위해서 사용된다.   (위 설명은 카멜 표기법 게시글에서도 언급한 바 있다)
```java
public class PascalTestClass // 파스칼 표기법
    {
    private int pascalValueTest; // 카멜 표기법
    public int PascalValueTest // 파스칼 표기법
    {
    get { return pascalValueTest; }
    private set { pascalValueTest= value; }
    }
    }
    // 변수는 카멜로 표기하고,
    // class, property 등은 파스칼로 표기하고 있다.​
```
### 스네이크 표기법(Snake case)
1. 단어를 언더바(_)로 구분하는 표기법
   - 다른 언어들과는 달리 파이썬의 경우  
언더바의 사용 의미가 다르다.
2. 카멜, 파스칼과는 반대로 언더바(_)를 사용하여 구분하고  
가독성을 높이기 위해 사용한다.
   - 파이썬의 경우
   1. 인터프리터(Interpreter)에서 마지막 값을 저장할 때
   2. 값을 무시하고 싶을 때 (흔히 “I don’t care”라고 부른다.)
   3. 변수나 함수명에 특별한 의미나 기능을 부여하고자 할 때
   4. 국제화(Internationalization, i18n)  
지역화(Localization, l10n) 함수로써 사용할 때
   5. 숫자 리터럴값의 자릿수 구분을 위한 구분자로 사용할 때
   - int item_count; int item_level;  
단어와 단어 사이를 언더바로 구분한다.