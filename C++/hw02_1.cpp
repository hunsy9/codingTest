#include <iostream>
#include <string>
#include <stack>

using namespace std;

class StringDecoder
{
private:
   string data_;

public:
   friend istream &operator>>(istream &is, StringDecoder &sd)
   {
      string input_Possible = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,!?@#$%^&*";
      stack<char> stack;
      string str;
      is >> str;
      int i = 0;
      while (i < str.size())
      {
         if (str[i] == '}')
         {
            string result = "";
            while (stack.top() != '{')
            {
               result = stack.top() + result;
               stack.pop();
            }
            stack.pop();
            if (!(stack.top() >= '0' && stack.top() <= '9' || stack.top() >= 'A' && stack.top() <= 'F'))
            {
               cout << "ERROR: Invalid input";
               sd.data_ = "";
               return is;
               stack.pop();
               break;
            }
            int getInt = (stack.top() >= '0' && stack.top() <= '9') ? stack.top() - '0' : stack.top() - 'A' + 10;
            stack.pop();
            for (int j = 1; j <= getInt; j++)
            {
               for (int x = 0; x < result.size(); x++)
               {
                  stack.push(result[x]);
               }
            }
         }
         else
         {
            stack.push(str[i]);
         }
         i++;
      }
      string ans = "";

      while (!stack.empty())
      {
         if (input_Possible.find(stack.top()) == string::npos)
         {
            cout << "ERROR: Invalid input";
            sd.data_ = "";
            return is;
            break;
         }
         ans = stack.top() + ans;
         stack.pop();
      }
      sd.data_ = ans;
      return is;
   }

   friend ostream &operator<<(ostream &os, const StringDecoder &sd)
   {
      os << sd.data_;
      return os;
   }
};

int main()
{
   StringDecoder sd;

   while (cin >> sd)
   {
      cout << sd;
   }
   return 0;
}