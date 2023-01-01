print("hello world")

msg = """This is \tline 1
This is \tline 2
He said "It's Christmas" """
print(msg)

print(msg.casefold())
msg2 = "Juniper Berries"
print(msg2[0:10:2])  # start, stop, step

print(msg2[::-1])   # reverse whole string

# f strings
txt = f'My message is {msg2}'
print(txt)

print(f"{msg2=}, {msg=}")
