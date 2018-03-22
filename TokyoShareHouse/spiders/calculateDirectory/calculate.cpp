#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

string filename = "newGetInfo.txt";

class sortWithPayment{
  private:
    string url;
    string name;
    string type;
    int payment;
  public:
    sortWithPayment(){}
    sortWithPayment(string u, string n, string t, int rent, int fee){
      url = u;
      name = n;
      type = t;
      payment = rent + fee;
    }
    int thisPayment(){
      return payment;
    }
    string printValue(){
      string str;
      str = url + "\n" + name + "\n" + type + "\n" + to_string(payment) + "\n\n";
      return str;
    }
    bool checkPrivate(){
      if (type == "Private")
        return true;
      return false;
    }
};

int changeStringToInt(string str){
  istringstream newone(str);
  string num;
  getline(newone, num, ',');
  return stoi(num)*1000;
}


vector<sortWithPayment> makeNewVector(){
  ifstream f(filename);
  string line;
  vector<sortWithPayment> newVector;
  while(getline(f, line)){
    string url = line;
    getline(f, line);
    string name = line;
    getline(f, line);
    string type = line;
    getline(f, line);
    string rent = line;
    getline(f, line);
    string fee = line;
    getline(f, line);
    getline(f, line);
    istringstream splittype(type);
    istringstream splitrent(rent);
    istringstream splitfee(fee);
    string t, r, f;
    if (type == "")
      continue;
    while(getline(splittype, t, '\t')){
      getline(splitrent, r, '\t');
      getline(splitfee, f, '\t');
      sortWithPayment newclass(url, name, t, changeStringToInt(r), changeStringToInt(f));
      newVector.push_back(newclass);
    }
  }
  return newVector;
}


bool compare_payment(sortWithPayment a, sortWithPayment b){
  return (a.thisPayment() < b.thisPayment());
}

int main(){
  vector<sortWithPayment> shareHouse;
  shareHouse = makeNewVector();
  sort(shareHouse.begin(), shareHouse.end(), compare_payment);

  ofstream out("output.txt");
  for (vector<sortWithPayment>::iterator i = shareHouse.begin(); i != shareHouse.end(); ++i)
    out << (*i).printValue();
  out.close();

  ofstream privateOut("private.txt");
  for (vector<sortWithPayment>::iterator i = shareHouse.begin(); i != shareHouse.end(); ++i){
    if ((*i).checkPrivate())
      privateOut << (*i).printValue();
  }
  privateOut.close();
  return 0;
}





