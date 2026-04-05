import numpy as np
def discreteStat():
    a=np.array(list(map(float,input("enter list of numbers:").split())))
    print("Mean:",np.mean(a),"\nMedian:",np.median(a),"\nVariance:",np.var(a),"\nStandard Deviation:",np.std(a),"\nMIN/MAX:",np.min(a),np.max(a),"\nRange:",np.ptp(a))
def correlationReg():
    x=np.array(list(map(float,input("Enter X values :").split())))
    y=np.array(list(map(float,input("Enter Y values :").split())))
    print("Correlation Coefficient:\n",np.corrcoef(x, y))
    slope,intercept=np.polyfit(x,y,1)
    print("Linear Regression :Y=", slope,"x+ ",intercept)
def probabilityDist():
    n=int(input("Enter Sample value:"))
    print("Normal Distribution:",np.random.normal(0,1,n),"\nBinomial Distribution:",np.random.binomial(10,0.5,n),"\nPoisson Distribution:",np.random.poisson(3,n),"\nUniform Distribution:",np.random.uniform(0,1,n))
def samplingTheory():
    a=np.array(list(map(float, input("Enter population data: ").split())))
    size=int(input("Enter sample size: "))
    sample = np.random.choice(a,size=size)
    print("Sample:",sample)
    print("Sample Mean:",np.mean(sample))
    print("Sample Variance:",np.var(sample))
while True:
    print("--------------------------")
    print("1. Descriptive Statistics")
    print("2. Correlation & Regression")
    print("3. Probability Distributions")
    print("4. Sampling Theory")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        discreteStat()
    elif choice=="2":
        correlationReg()
    elif choice=="3":
        probabilityDist()
    elif choice=="4":
        samplingTheory()
    elif choice=="5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
        break
    