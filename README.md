# Weather-Forecast-API
A web-application that was built through JavaScript and Django Framework using Web API. The development lifecycle was build using Scrum Agile Framework. Conducted testing using Atheris Fuzzing engine.


I implemented API using JavaScript and Django. Django was used for server-side API implementation and JavaScript for the client-side. 


### Testing

To test the web-application, open terminal and copy the following line: 
```
python -m test
```

### Import the Atheris library

If you do not have Atheris Fuzzing Enginer, do the following. 

Clone the github repository: 
```
git clone https://github.com/llvm/llvm-project.git
cd llvm-project
mkdir build
cd build
cmake -DLLVM_ENABLE_PROJECTS='clang;compiler-rt' -G "Unix Makefiles" ../llvm
make -j 10  
```
Install:
```
CLANG_BIN="$(pwd)/bin/clang" pip3 install <whatever>
```

### Explaining what the Fuzzing Testing Code does

First function of my Testing Code is:
```
def fuzz_testing(data):
    ....
```

In general, this function tests the response and request flow of my API. It sends random data to our API and it triggers the error response (HTTP Bad request). My goal was to check the API for data validation. 

Second function of my Testing Code is:
```
def data_wrangling(data):
     ....
```

Generally, this function tests whether we have inputted correct data type, which is string. If so, there is no error. If the input data is non-string, we throw an Error Non-string input triggered. 

### Atheris Fuzzing

At the end of the testing, we can start testing with Atheris through the following lines: 
```
atheris.Setup()
atheris.Fuzz(fuzz_testing, data_wrangling)
```

That is all! Thanks for reading this. 
