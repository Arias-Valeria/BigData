fibonacci <- c();

for(j in 1:20)
{
  if(j == 1)
  {
    fibonacci <- c(fibonacci, 0);
    
  }
  else if(j > 2)
  {
    fibonacci <- c(fibonacci, fibonacci[j-1] + fibonacci[j-2]);
  }
  else
  {
    fibonacci <- c(fibonacci, 1);
  }
}
print('Serie Fibonacci: ');

print(fibonacci)
