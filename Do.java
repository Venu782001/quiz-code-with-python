class DO
{
 void add()
{
 int a=10;
 int b=20;
 int c=a+b;
System.out.println(c);
}
 void add(int X,int Y,int Z)
{
 int g=X+Y+Z;
}
}
class Cai
{
public static void main(String args[])
{
   Do os=new Do();
   os.add();
   os.add(10,20,30);
}
}