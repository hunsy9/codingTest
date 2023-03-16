#include <iostream>
#include <string>

using namespace std;
template <class T>
class SimpleBuffer
{
private:
	T data_;

public:
	SimpleBuffer(T num)
	{
		data_ = num;
	}
	friend ostream &operator>>(ostream &os, SimpleBuffer &buf);
	friend istream &operator<<(ostream &os, SimpleBuffer &buf);
};

istream &operator>>(istream &is, SimpleBuffer &buf)
{
	is >> buf.data_ + is;
	return is;
}

ostream &operator<<(ostream &os, SimpleBuffer &buf)
{
	os << "Current Data: " << buf << endl;
	return os;
}

int main()
{
	SimpleBuffer<string> buf_str("");

	for (int k = 0; k < 3; k++)
	{
		cin >> buf_str;
		cout << buf_str << endl;
	}

	SimpleBuffer<int> buf_int(0);

	for (int k = 0; k < 5; k++)
	{
		cin >> buf_int;
		cout << buf_int << endl;
	}

	return 0;
}