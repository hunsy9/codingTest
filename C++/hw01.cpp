#include <iostream>
#include <string>

using namespace std;

// Your class SimpleBuffer
template <class T>
class SimpleBuffer{
	private:
		T data_;
	
	public:	
    SimpleBuffer();
		buf_str(T _data);
		buf_int(T _data);
};

T buf_int(T _data){
	_data+=_data;
}

int main() {
	SimpleBuffer<string> buf_str("");
	
	for(int k = 0; k < 3; k++){
		cin >> buf_str;
		cout << buf_str << endl;
	}
	
	SimpleBuffer<int> buf_int(0);
	
	for(int k = 0; k < 5; k++){
		cin >> buf_int;
		cout << buf_int << endl;
	}
	
	return 0;
}