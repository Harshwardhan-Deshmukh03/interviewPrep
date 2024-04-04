
import json
import requests
import time

CODE_EVALUATION_URL = 'https://api.hackerearth.com/v4/partner/code-evaluation/submissions/'
GET_STATUS_URL = 'https://api.hackerearth.com/v4/partner/code-evaluation/submissions/'
CLIENT_SECRET = 'cf376beb1b851511a1f24a45dffb923250e2beb2'


def lookup(num):
    """
    values will have language,code, boilerplate
    """
    values={
        1:["C","C",'#include <stdio.h>\nint main() {\n // Write C code here\n    printf("Hello world");\n\n    return 0;\n}\n'],
        2:["C++14","CPP14",'#include <iostream>\n int main() { \n // Write C++ code here \nstd::cout << "Hello world!";\nreturn 0; \n}'],
        3:["C++17","CPP17",'#include <iostream>\n\nint main() {\n    // Write C++ code here\n    std::cout << "Hello world!";\n\n    return 0;\n}\n'],
        10:["Clojure","CLOJURE",'(defn -main []\n  (println "Hello world"))\n'],
        11:["C#","CSHARP",'using System;\n\nclass HelloWorld {\n    static void Main() {\n        Console.WriteLine("Hello, World!");\n    }\n}\n'],
        12:["GO","GO",'package main\n\nimport "fmt"\n\nfunc main() {\n    // Write Go code here\n    fmt.Println("Hello world")\n}\n'],
        13:["Haskell","HASKELL",'main = putStrLn "Hello, World!"\n'],
        4:["JAVA 8","JAVA8",'class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}\n'],
        5:["JAVA 14","JAVA14",'class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}\n'],
        14:["JavaScript(Nodejs)","	JAVASCRIPT_NODE",'console.log("Hello, World!");\n'],
        6:["Kotlin","KOTLIN",'fun main() {\n    println("Hello, World!")\n}\n'],
        15:["Objective C","OBJECTIVEC",'#import <Foundation/Foundation.h>\n\nint main() {\n    @autoreleasepool {\n        NSLog(@"Hello, World!");\n    }\n    return 0;\n}\n'],
        16:["Pascal","PASCAL","program HelloWorld;\nbegin\n  writeln('Hello, World!');\nend.\n"],
        17:["Perl","PERL",'#!/usr/bin/perl\n\nprint "Hello, World!\n";\n'],
        18:["PHP","PHP",'<?php\necho "Hello, World!";\n?>\n'],
        7:["Python 2","PYTHON",'print "Hello, World!"'],
        8:["Python 3","PYTHON3",'print("Hello, World!")'],
        9:["Python 3.8","PYTHON3_8",'print("Hello, World!")'],
        19:["R","R",'message <- "Hello, World!" \nprint(message)'],
        20:["Ruby","RUBY",'puts "Hello, World!"'],
        21:["Rust","RUST",'fn main() {  println!("Hello, World!"); }'],
        22:["Scala","SCALA",'object HelloWorld {\n  def main(args: Array[String]) {\n    println("Hello, World!")\n  }\n}\n'],
        23:["Swift","SWIFT",'print("Hello, World!")'],
        24:["TypeScript","TYPESCRIPT",'console.log("Hello, World!");'],
    }

    return values.get(num)




def execute_and_get_status( language,source,input):
    # Execute the code
    source = source
    input_file = input
    callback = "https://client.com/callback/"
    TIME_LIMIT = 15
    data = {
        'source': source,
        'lang': language,
        'time_limit': TIME_LIMIT,
        'memory_limit': 246323,
        'input': input_file,
        'callback': callback,
        'id': "client-001"
    }
    headers = {"client-secret": CLIENT_SECRET}
    
    resp = requests.post(CODE_EVALUATION_URL, json=data, headers=headers)
    response_dict = json.loads(resp.text)
    print(response_dict)
    url_of_answer = response_dict['status_update_url']

    time.sleep(TIME_LIMIT)

    status_resp = requests.get(GET_STATUS_URL + response_dict['he_id'] + '/', headers=headers)
    status_dict = json.loads(status_resp.text)

    output_url = status_dict['result']['run_status']['output']
    output_resp = requests.get(output_url)
    final_output = output_resp.content.decode('utf-8')

    return final_output


def output_response_ide(lang_code,code_to_run,inputs):
    return execute_and_get_status(lang_code,code_to_run,inputs)