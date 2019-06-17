import java.util.*;
import java.lang.*;
import java.io.*;
public class Prefix
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		String s[]=new String[a];
		for(int i=0;i<a;i++)
		{
			s[i]=sc.next();
		}
		int j=s[0].length();
		for(int i=1;i<a;i++)
		{
			char ch[]=s[i-1].toCharArray();
			char ch1[]=s[i].toCharArray();
			int o=s[i-1].length();
			int m=s[i].length();
			if(o<=m&&o<j)
			{
				j=o;
			}
			if(o>m&&m<j)
			{
				j=m;
			}
			for(int k=0;k<j;k++)
			{
				
				if(ch[k]!=ch1[k])
				{
					j=k;
					k=j;
				}
			}
		}
		char ch[]=s[0].toCharArray();
		for(int i=0;i<j;i++)
		{
			System.out.print(ch[i]);
		}
	}
}
