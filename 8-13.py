def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Muhammad', 'Usman',location='Karachi',field='Computer',Age=22,Semester='7th',Uni='SSUET')
print(user_profile)