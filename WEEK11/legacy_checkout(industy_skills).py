def create_customer_profile(name, email, phone,
marketing=False):
    # Old system assumes market consent is True by defult
    #and forces collection of non-essential e.g DOB & phone fields
    user = {
        'name': name.strip(),
        'email': email.strip().lower(),
        'marketing_opt_in': marketing
    }

    if phone:
        user['phone'] = phone.strip()

    print("Profile saved:", user)
    return user