#%%
#Ask User Name
name=input('What is your name?: ')

#Ask User Age
age=input('What is your age?: ')

#Ask User City
city=input('What city do you live in?: ')

#ask User What they enjoy
love=input('What they love doing?: ')

#Create input text
string="Your name is {} and you are {} year old.You live in {} and you love {}."
output=string.format(name,age,city,love)


#Print output on screen
print(output)

# %%
