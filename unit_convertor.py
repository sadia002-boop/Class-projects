import streamlit as st
# 1-unit converter application
# 2-input for unit convertor
# 3-output given by unit convertor application

# inouts
# 1-value
# 2-unit from converstion / kis unit sy convert karna ha 
# 3-unit to conversion / kis unit main convert karna ha 

# value unit_from  unit_to
#20000 meters       kilometers


# output
# converted value in preffered unit type

#
def convert_units(value: float, unit_from: str, unit_to: str):
    #print("value>>>", value) 
    #print("value_from>>>", unit_from) 
    #print("value_to>>>", unit_to) 

    # 1 kilometer = 1000 meters
    # 1 meter = 0.001 kilometer
    # 1 kilogram = 1000 grams
    # 1 gram = 0.001 kilogram
    # value hu tu kilometers main or value convert karni ho meters
    if unit_from == "kilometers" and unit_to == "meters":
          #  1.5 * 1000
          return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        #  1 * 0.001 = 0.001 kilometer
        return value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
    # 2 * 1000 = 2000
        return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
         return value * 0.001
    else :
         return "conversion is not supported!"


# # result = output ki value 
# result1=convert_unites(1.5, "kilometer", "meter")
# print("the result in meter is", result1)
# result2 = convert_unites(5000,"grams", "kilograms")
# print("the value is kilograms is", result2)




def main():
    st.title("unit convertor")
    st.write("welcome to unit converter")

    value = st.number_input("enter the value you want to convert:")
    unit_from = st.text_input("enter the unit you want to convert from (e.g meters, kilometers, grams, kilograms)")
    unit_to = st.text_input("enter the unit you want from conversion (e.g meters, kilometers, grams, kilograms)")

    st.button("convert")
    result = convert_units(value, unit_from, unit_to)

    st.write("converted value is :" ,result)

  #  print("unit converter")
  #print("welcome to unit converter!")

#value = float(input("enter the value you want to convert:")) # 1 -> 1.00 1 -> 1.5
#unit_from = input("enter the unit you want to convert from (e.g meters, kilometers, grams, kilograms)")
#unit_to = input("enter the unit you want from conversion (e.g meters, kilometers, grams, kilograms)")

#print("value>>>>", value)
#print("unit_to>>>>",unit_to)
#print("unit_from>>>>",unit_from)
#result = convert_units( value, unit_from, unit_to)
#print("converted value is :", result)

main()