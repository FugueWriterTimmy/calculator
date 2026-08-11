def conjugate_lithuanian(infinitive, pres_3, past_3):
    inf = infinitive.strip().lower()
    pres_3 = pres_3.strip().lower()
    past_3 = past_3.strip().lower()
    
    inf_stem = inf[:-2] if inf.endswith('ti') else inf
    
    pres_ending = pres_3[-1]
    pres_stem = pres_3[:-1]
    
    past_ending = past_3[-1]
    past_stem = past_3[:-1]
    
    pres_forms = {}
    if pres_ending == 'a':
        # Check if the stem ends in 'i' to prevent double 'ii' in 2sg
        sg2_ending = "" if pres_stem.endswith('i') else "i"
        pres_forms = {"1sg": pres_stem + "u", "2sg": pres_stem + sg2_ending, "3sg": pres_3, "1pl": pres_stem + "ame", "2pl": pres_stem + "ate"}
        pres_forms["3pl"] = pres_stem + "ą"
    elif pres_ending == 'i':
        pres_forms = {"1sg": pres_stem + "iu", "2sg": pres_stem + "i", "3sg": pres_3, "1pl": pres_stem + "ime", "2pl": pres_stem + "ite"}
        pres_forms["3pl"] = pres_stem + "į"
    elif pres_ending == 'o':
        pres_forms = {"1sg": pres_stem + "au", "2sg": pres_stem + "ai", "3sg": pres_3, "1pl": pres_stem + "ome", "2pl": pres_stem + "ote"}
        pres_forms["3pl"] = pres_stem + "ą"
        
    past_forms = {}
    if past_ending == 'o':
        past_forms = {"1sg": past_stem + "au", "2sg": past_stem + "ai", "3sg": past_3, "1pl": past_stem + "ome", "2pl": past_stem + "ote"}
        past_forms["3pl"] = past_stem + "ų" 
    elif past_ending == 'ė':
        p_stem = past_stem
        if p_stem.endswith('t'): p_stem = p_stem[:-1] + 'č'
        elif p_stem.endswith('d'): p_stem = p_stem[:-1] + 'dž'
        
        past_forms = {"1sg": p_stem + "iau", "2sg": past_stem + "ei", "3sg": past_3, "1pl": past_stem + "ėme", "2pl": past_stem + "ėte"}
        past_forms["3pl"] = past_stem + "ę"

    ph_stem = inf_stem + "dav"
    ph_forms = {
        "1sg": ph_stem + "au", "2sg": ph_stem + "ai", "3sg": ph_stem + "o",
        "1pl": ph_stem + "ome", "2pl": ph_stem + "ote", "3pl": ph_stem + "ą"
    }

    fut_stem = inf_stem
    if fut_stem.endswith(('š', 'ž')):
        fut_stem = fut_stem[:-1] + 'š'
    elif fut_stem.endswith(('s', 'z', 't', 'd')):
        fut_stem = fut_stem[:-1] + 's'
    else:
        fut_stem = fut_stem + 's'
        
    fut_forms = {
        "1sg": fut_stem + "iu", "2sg": fut_stem + "i", "3sg": fut_stem + "",
        "1pl": fut_stem + "ime", "2pl": fut_stem + "ite", "3pl": fut_stem + "į"
    }

    cond_stem = inf_stem
    cond_forms = {
        "1sg": cond_stem + "čiau", "2sg": cond_stem + "tum", "3sg": cond_stem + "tu",
        "1pl": cond_stem + "tume", "2pl": cond_stem + "tute", "3pl": cond_stem + "tų"
    }

    imp_stem = inf_stem
    if imp_stem.endswith(('k', 'g', 't', 'd')):
        imp_stem = imp_stem[:-1] + 'k'
    else:
        imp_stem = imp_stem + 'k'
        
    imp_forms = {
        "1sg": imp_stem + "iu", "2sg": imp_stem + "",  "3sg": "te" + pres_3,
        "1pl": imp_stem + "ime", "2pl": imp_stem + "ite", "3pl": "te" + pres_forms["3pl"]
    }

    tenses = {
        "Present": pres_forms, "Past": past_forms, "Past Habitual": ph_forms,
        "Future": fut_forms, "Conditional": cond_forms, "Imperative": imp_forms
    }
    
    for tense, forms in tenses.items():
        print(f"\n--- {tense} ---")
        for person, form in forms.items():
            print(f"{person}: {form}")

# Example test with an -ia verb (e.g., studijuoti -> studijuoja)
conjugate_lithuanian("traukti", "traukia", "traukė")
