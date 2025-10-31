def calculate_study_points(subject_type, hours_studied, difficulty_level):
    if subject_type == "mathematics":
        if difficulty_level == "low":
            points_per_hour = 12
        elif difficulty_level == "medium":
            points_per_hour = 18
        elif difficulty_level == "high":
            points_per_hour = 25
        else:
            return "Wrong type of level"
    elif subject_type == "sciences":
        if difficulty_level == "low":
            points_per_hour = 10
        elif difficulty_level == "medium":
            points_per_hour = 15
        elif difficulty_level == "high":
            points_per_hour = 20
        else:
            return "Wrong type of level"
    else:  
        if difficulty_level == "low":
            points_per_hour = 8
        elif difficulty_level == "medium":
            points_per_hour = 12
        elif difficulty_level == "high": 
            points_per_hour = 16
        else:
            return "Wrong type of level"

    return points_per_hour * hours_studied

def calculate_mastery_index(semester_count, baseline_score, current_score):
    expected_score = 1000 + (semester_count * 100)
    score_range = expected_score - baseline_score
    mastery_percentage = (current_score - baseline_score) / score_range * 100
    return mastery_percentage

def determine_progress_tier(mastery_percent):
    if mastery_percent < 50:
        return "Foundation Tier"
    elif mastery_percent < 60:
        return "Development Tier"
    elif mastery_percent < 70:
        return "Proficiency Tier"
    elif mastery_percent < 85:
        return "Excellence Tier"
    else:
        return "Mastery Tier"
    

def calculate_achievement_score(points, hours, tier_modifier):
    base_score = points * 0.05 + hours * 2
    
    if tier_modifier  == "Foundation Tier":
        tier_modifier = 0.5
    elif tier_modifier  == "Development Tier":
        tier_modifier = 1.0
    elif tier_modifier  == "Proficiency Tier":
        tier_modifier = 1.2  
    elif tier_modifier  == "Excellence Tier":
        tier_modifier = 1.5
    elif tier_modifier  == "Mastery Tier":  
        tier_modifier = 1.8
    else:
        return ("Wrong Type of Tier")
    final_score = base_score * tier_modifier
    return round(final_score, 1)

def needs_tutoring(study_weeks, total_hours, avg_mastery):
    if study_weeks >= 6 and avg_mastery < 50:
        return "Yes"
    elif total_hours < 100 and avg_mastery < 60:
        return "Yes"
    elif study_weeks >= 4 and avg_mastery < 40:
        return "Yes"
    else: 
        return "No"
    
def generate_progress_report(student, subject_type, hours, difficulty_level, semester_count, baseline_score, current_score, study_weeks):
    study_points = calculate_study_points(subject_type, hours, difficulty_level)
    mastery_index = calculate_mastery_index(semester_count, baseline_score, current_score)
    progress_tier = determine_progress_tier(mastery_index)
    achievement_score = calculate_achievement_score(study_points, hours, progress_tier)
    tutoring = needs_tutoring(study_weeks, hours, mastery_index)

    print("========================================")
    print(f"Progress Report for: {student}")
    print("----------------------------------------")
    print(f"Subject Type: {subject_type}")
    print(f"Hours Studied: {hours}")
    print(f"Difficulty Level: {difficulty_level}")
    print(f"Study Points: {study_points}")
    print(f"Mastery Analysis:")
    print(f"  Semesters: {semester_count}, Baseline: {baseline_score}, Current Score: {current_score}")
    print(f"  Mastery: {round(mastery_index, 1)}%")
    print(f"Progress Tier: {progress_tier}")
    print(f"Achievement Score: {achievement_score}")
    print(f"Study Weeks: {study_weeks}")
    print(f"Tutoring Needed: {tutoring}")
    print()
    
print("ACADEMIC PROGRESS TRACKER")
print("========================================")

generate_progress_report("Parker", "mathematics", 45 , "high", 3, 800, 1150, 3)
generate_progress_report("Riley", "sciences", 60, "medium", 5, 900, 1300, 5)
generate_progress_report("Cameron", "languages", 30 , "low", 8, 850, 950, 7)

