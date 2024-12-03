{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e8dacd88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 5 8 13 21 34 55 89 \n"
     ]
    }
   ],
   "source": [
    "n=10\n",
    "num1=0\n",
    "num2=1\n",
    "next_number=num2\n",
    "count=1\n",
    "while count<=n:\n",
    "    print(next_number,end=\" \")\n",
    "    count +=1\n",
    "    num1,num2=num2,next_number\n",
    "    next_number=num1+num2\n",
    "print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3f75b903",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "employee details\n",
      "name:john\n",
      "name:chandu\n",
      "name:tanu\n",
      "total salary:16600is total salary of all\n",
      "5533.333333333333is average salary of all\n"
     ]
    }
   ],
   "source": [
    "employees=[\n",
    "    {\"name\":\"john\",\"salary\":5000},\n",
    "    {\"name\":\"chandu\",\"salary\":5600},\n",
    "    {\"name\":\"tanu\",\"salary\":6000},\n",
    "]\n",
    "total_salary=sum(emp[\"salary\"] for emp in employees)\n",
    "average_salary=total_salary/len(employees)\n",
    "print(\"employee details\")\n",
    "for emp in employees:\n",
    "    print(f\"name:{emp['name']}\")\n",
    "print(f\"total salary:{total_salary}is total salary of all\")\n",
    "print(f\"{average_salary}is average salary of all\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3a9848d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "matrix sum:\n",
      " [[ 6  8]\n",
      " [10 12]]\n",
      "matrix product:\n",
      " [[19 22]\n",
      " [43 50]]\n",
      "solution to Ax=B: [2. 3.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import linalg\n",
    "#define two matrices\n",
    "matrix1=np.array([[1,2],[3,4]])\n",
    "matrix2=np.array([[5,6],[7,8]])\n",
    "#matrix operations \n",
    "matrix_sum=matrix1+matrix2\n",
    "matrix_product=np.dot(matrix1,matrix2)\n",
    "print(\"matrix sum:\\n\",matrix_sum)\n",
    "print(\"matrix product:\\n\",matrix_product)\n",
    "#solve a system of linear equations:Ax=B\n",
    "A=np.array([[3,1],[1,2]])\n",
    "B=np.array([9,8])\n",
    "solution=linalg.solve(A,B)\n",
    "print(\"solution to Ax=B:\",solution)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f1fbbb6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
