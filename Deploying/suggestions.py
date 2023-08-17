def Kidney_Sug(dis_name):
    k_symt = ["Fatigue and weakness","Swelling of feet and ankles","High blood pressure","Nausea and vomiting","Changes in urine frequency, color and in some cases blood in urine","Muscle cramps or twitches"]
    k_pres = ["Medications to control high blood pressure","Fluid management","Dietary and lifestyle changes","Dialysis","Kidney transplant"]
    k_pcau = ["Monitoring blood pressure","Managing blood sugar level","Avoiding nephrotoxic substances","Hygiene and infection prevention","Following a renal-friendly diet"]
    if dis_name != "Normal":
        line1 = "The following CT-Scan Image has been Identified as <strong>" + dis_name + "</strong>"
        line2 = "\n\n◉ <strong>Symptoms</strong>"
        for l2 in k_symt:
            line2 +=  "\n\t\t\t➣ " + l2 
        line3 = "\n\n◉ <strong>Suggested Medication</strong>"
        for l3 in k_pres:
            line3 +=  "\n\t\t\t➣ " + l3
        line4 = "\n\n◉ <strong>Precautions</strong>"
        for l4 in k_pcau:
            line4 +=  "\n\t\t\t➣ " + l4
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line2 + line3 + line4 + line5
    elif dis_name == "Normal":
        line1 = "The following CT-Scan Image seems to be <strong>" + dis_name + "</strong>"
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line5
    else:
        line1 = "The following CT-Scan Image was not able to classify in any of the Kidney related Diseases"
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line5
    return line

def Brain_Sug(dis_name):
    k_symt = ["Headaches","Cognitive or neurological changes","Behavioral or mood changes","Nausea and vomiting","fatigue and weakness"]
    k_pres = ["Surgery","Radiation therapy","Chemotherapy","Targeted therapy","Corticosteroids"]
    k_pcau = ["Regular check-ups","Practice healthy lifestyle habits","Avoid exposure to harmful substances","Follow prescribed treatment plan","Seek medical attention for concerning symptoms"]
    if dis_name != "Notumor" and dis_name != "None":
        line1 = "The following CT-Scan Image has been Identified as <strong>" + dis_name + "</strong>"
        line2 = "\n\n◉ <strong>Symptoms</strong>"
        for l2 in k_symt:
            line2 +=  "\n\t\t\t➣ " + l2 
        line3 = "\n\n◉ <strong>Suggested Medication</strong>"
        for l3 in k_pres:
            line3 +=  "\n\t\t\t➣ " + l3
        line4 = "\n\n◉ <strong>Precautions</strong>"
        for l4 in k_pcau:
            line4 +=  "\n\t\t\t➣ " + l4
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line2 + line3 + line4 + line5
    elif dis_name == "Notumor":
        line1 = "The following CT-Scan Image seems to be <strong> Normal </strong>"
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line5
    else:
        line1 = "The following CT-Scan Image was not able to classify in any of the Brain related Diseases"
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line5
    return line

def Lungs_Sug(dis_name):
    k_symt = ["Persistent cough","Shortness of breath","Fatigue and chest pain","Respiratory infections","Changes in sputum or coughing up blood","chest tightness or discomfort","changes in voice"]
    k_pres = ["Medications to manage symptoms","Oxygen therapy","Pulmonary rehabilitation","Immunizations","Targeted therapies"]
    k_pcau = ["Avoiding smoking and exposure to smoke","Reducing exposure to air pollutants","following prescribed treatment plans","Monitoring symptoms","Avoiding respiratory infections"]
    if dis_name != "Normal" and dis_name != "None":
        line1 = "The following CT-Scan Image has been Identified as <strong>" + dis_name + "</strong>"
        line2 = "\n\n◉ <strong>Symptoms</strong>"
        for l2 in k_symt:
            line2 +=  "\n\t\t\t➣ " + l2 
        line3 = "\n\n◉ <strong>Suggested Medication</strong>"
        for l3 in k_pres:
            line3 +=  "\n\t\t\t➣ " + l3
        line4 = "\n\n◉ <strong>Precautions</strong>"
        for l4 in k_pcau:
            line4 +=  "\n\t\t\t➣ " + l4
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line2 + line3 + line4 + line5
    elif dis_name == "Normal":
        line1 = "The following CT-Scan Image seems to be <strong>" + dis_name + "</strong>"
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line5
    else:
        line1 = "The following CT-Scan Image was not able to classify in any of the Lungs related Diseases"
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line5
    return line

def Tuber_Sug(dis_name):
    k_symt = ["Persistent cough","Chest pain","Fatigue","Weight loss","Fever and chills","Breathlessness"]
    k_pres = ["Isoniazid","Rifampin","Pyrazinamide","Ethambutol","Streptomycin"]
    k_pcau = ["Take medications as prescribed","Follow infection control measure","Avoid close contact with other","Practice good hygien","Stay informed","Get screened"]
    if dis_name != "None" and dis_name != "Normal":
        line1 = "The following CT-Scan Image has been Identified as Postive for <strong>Tuberculosis</strong>"
        line2 = "\n\n◉ <strong>Symptoms</strong>"
        for l2 in k_symt:
            line2 +=  "\n\t\t\t➣ " + l2 
        line3 = "\n\n◉ <strong>Suggested Medication</strong>"
        for l3 in k_pres:
            line3 +=  "\n\t\t\t➣ " + l3
        line4 = "\n\n◉ <strong>Precautions</strong>"
        for l4 in k_pcau:
            line4 +=  "\n\t\t\t➣ " + l4
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line2 + line3 + line4 + line5
    elif dis_name == "Normal":
        line1 = "The following CT-Scan Image has been Identified as Negative for <strong>Tuberculosis</strong>"
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line5
    else:
        line1 = "The following CT-Scan Image was not able to classify in any of the Tuberculosis related Diseases"
        line5 = "\n\n<strong>Disclaimer</strong>: This is Machine Generated Analysis, Please consult any Physician before taking any step."
        line = line1 + line5
    return line
