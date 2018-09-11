import java.util.Scanner;
public class test2{
public static void main(String [] args){
System.out.println("陣列");
int[] x=new int[10];
for(int i=0;i<5;i++){
x[i]=i;
System.out.println(x[i]);
}
System.out.println("在第3個元素插入5");
for(int j=4;j>1;j--)
{
x[j+1]=x[j];
}
x[2]=5;
for(int i=0;i<10;i++){ 
System.out.println(x[i]);
}
System.out.println("刪除第4個元素");
for(int k=4;k<7;k++){
x[k-1]=x[k];
}
for(int i=0;i<10;i++){ 
System.out.println(x[i]);
}
}	  	
}