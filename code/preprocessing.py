import pandas as pd

# CSV 파일 경로
csv_file_path = "/mnt/data/synthetic_data.csv"

# CSV 파일 불러오기
df = pd.read_csv(csv_file_path)

# SQL 파일 생성 경로
sql_file_path = "/mnt/data/synthetic_data.sql"

# 테이블 생성 쿼리
create_table_query = """
CREATE TABLE IF NOT EXISTS suicide_data (
    year INT,
    region VARCHAR(50),
    unemployment_rate FLOAT,
    household_income FLOAT,
    poverty_rate FLOAT,
    gini_index FLOAT,
    divorce_rate FLOAT,
    domestic_violence_reports INT,
    education_level FLOAT,
    population_density FLOAT,
    mental_health_issue_rate FLOAT,
    substance_abuse_rate FLOAT,
    psychiatric_hospitalization_rate FLOAT,
    suicide_attempt_hospital_visits INT,
    religious_participation_rate FLOAT,
    social_support_index FLOAT,
    social_stigma_index FLOAT,
    mental_health_budget FLOAT,
    suicide_prevention_program BOOLEAN,
    mental_health_service_accessibility FLOAT,
    suicide_rate FLOAT
);
"""

# 데이터 삽입 쿼리 준비
insert_queries = []
for _, row in df.iterrows():
    insert_query = f"""
    INSERT INTO suicide_data (
        year, region, unemployment_rate, household_income, poverty_rate, gini_index,
        divorce_rate, domestic_violence_reports, education_level, population_density,
        mental_health_issue_rate, substance_abuse_rate, psychiatric_hospitalization_rate,
        suicide_attempt_hospital_visits, religious_participation_rate, social_support_index,
        social_stigma_index, mental_health_budget, suicide_prevention_program,
        mental_health_service_accessibility, suicide_rate
    ) VALUES (
        {int(row['연도'])}, '{row['지역']}', {row['실업률']}, {row['가계 소득']}, {row['빈곤율']},
        {row['지니계수']}, {row['이혼율']}, {int(row['가정 폭력 신고 건수'])}, {row['교육 수준']},
        {row['인구 밀도']}, {row['정신 건강 문제 발생률']}, {row['알코올 및 약물 남용률']},
        {row['정신과 입원율']}, {int(row['자살 시도 병원 방문 건수'])}, {row['종교 참여율']},
        {row['사회적 지원 수준']}, {row['사회적 낙인 정도']}, {row['정신 건강 지원 예산']},
        {1 if row['자살 예방 프로그램 존재 여부'] else 0}, {row['정신 건강 서비스 접근성']}, {row['자살률']}
    );
    """
    insert_queries.append(insert_query)

# SQL 파일 저장
with open(sql_file_path, "w", encoding="utf-8") as sql_file:
    sql_file.write(create_table_query)
    sql_file.write("\n".join(insert_queries))

# 결과 파일 경로 출력
print(f"SQL 파일이 생성되었습니다: {sql_file_path}")

