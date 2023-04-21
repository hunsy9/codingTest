schools = ["부산대학교", "동아대학교", "부산카톨릭대학교", "신라대학교", "창민대학교", "승훈대학교", "준우대학교", "재안대학교"]  # 0~7 인덱스 참고용으로 만들어 놓음
gender = ["여자","남자"] #1번 무조건필터
schoolFilter = ["자대","타대","상관없음"] #2번 무조건 필터
preferenceFilter = ["경영경제", "인문사회" ,"공학", "자연과학", "교육", "의료", "예체능", "기타", "상관없음"]
avoidOurTeamMajors = ["피하기", "상관없음"] #3번 무조건 필터
class AllTeamData:
    def __init__(self):
        self.AllTeamData = []
    def add(self,team):
        self.AllTeamData.append(team)
    def printAllTeams(self):
        for team in self.AllTeamData:
            team.printTeam()
class Team:
    def __init__(self, teamId, teamGender, teamSchoolIndexList, schoolFilter, preferenceFilter, avoidOurTeamMajors):
        self.teamId = teamId #팀 아이디
        self.teamGender = teamGender #팀 구성원들의 성별 -> 남자는 1, 여자는 0
        self.teamSchoolIndexList = teamSchoolIndexList # 팀원들의 학교 인덱스 리스트 ex) [1,3,5] 0~7중에 하나
        self.schoolFilter = schoolFilter # 자대만/ 타대만 / 상관없음 [0,1,2]중 하나
        self.preferenceFilter = preferenceFilter # 선호계열 경영경제/인문사회/공학/자연과학/교육/의료/예체능/기타/상관없음 [0~7] 중에 세 개 선택되거나 상관없음(8)
        self.avoidOurTeamMajors = avoidOurTeamMajors # 본인 팀원들 계열 피하기-> 피하기(1), 본인팀원들 전공계열 만나도 상관없다(0)
    def printTeam(self):
        teamMemberSchools = [schools[i] for i in self.teamSchoolIndexList]
        preference = [preferenceFilter[i] for i in self.preferenceFilter]
        print("----------------------------------------------------------")
        print("teamId: {}, 팀원들 성별: {}, 팀원들의 학교: {}".format(self.teamId, gender[self.teamGender], teamMemberSchools))
        print("자대/타대 필터: {}, 선호계열: {}, 팀원들 전공 피하기: {}".format(schoolFilter[self.schoolFilter],preference,avoidOurTeamMajors[self.avoidOurTeamMajors]))
