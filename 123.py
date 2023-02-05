hrs = input('Enter hours:')
rate = input('Enter rate:')
fhrs = float(hrs)
frate = float(rate)
if fhrs > 40 :
    print ('Overtime')
    regpay = fhrs * frate
    otpay = (fhrs - 40.0) * (frate * 0.5)
    print (regpay, otpay)
    pagofinal = regpay + otpay
else:
    print ('Regular')
    pagofinal = fhrs * frate
print ('Pay:', pagofinal)

