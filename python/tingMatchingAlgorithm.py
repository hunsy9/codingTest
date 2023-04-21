import teamClass

teams = teamClass.AllTeamData()
girlTeamWithSchoolNotMind=[]
boyTeamWithSchoolNotMind=[]
girlTeamWithMySchool=[]
boyTeamWithMyScool=[]
girlTeamWithOtherSchool=[]
boyTeamWithOtherSchool=[]

left=[]

def dataInitialize():
    teamDatas = open("match_test_case.txt", 'r')
    for teamData in teamDatas:
        e = list(map(str, teamData.split()))
        teamSchoolIndexList = list(map(int, e[2].split(",")))
        preferenceFilter = list(map(int, e[4].split(",")))
        teams.add(teamClass.Team(int(e[0]),int(e[1]),teamSchoolIndexList,int(e[3]),preferenceFilter,int(e[5])))
def divideTeamBySchoolFilter(teams):
    for i in teams.AllTeamData: ##teams.AllTeamData로 매칭신청 중인 팀들이 모여있는 리스트 접근가능
        if i.teamGender == 1:
            if i.schoolFilter == 0:
                boyTeamWithMyScool.append(i)
            if i.schoolFilter == 1:
                boyTeamWithOtherSchool.append(i)
            if i.schoolFilter == 2:
                boyTeamWithSchoolNotMind.append(i)
        else:
            if i.schoolFilter == 0:
                girlTeamWithMySchool.append(i)
            if i.schoolFilter == 1:
                girlTeamWithOtherSchool.append(i)
            if i.schoolFilter == 2:
                girlTeamWithSchoolNotMind.append(i)
    print("boyTeamWithMyScool: ",len(boyTeamWithMyScool))
    print("boyTeamWithOtherSchool: ",len(boyTeamWithOtherSchool))
    print("boyTeamWithSchoolNotMind: ",len(boyTeamWithSchoolNotMind))
    print("girlTeamWithMySchool: ",len(girlTeamWithMySchool))
    print("girlTeamWithOtherSchool: ",len(girlTeamWithOtherSchool))
    print("girlTeamWithSchoolNotMind: ",len(girlTeamWithSchoolNotMind))

def match(boyTeams,girlTeams):
    for boyTeam,girlTeam in zip(boyTeams,girlTeams):
        boyTeam

dataInitialize()
divideTeamBySchoolFilter(teams)
match(boyTeamWithSchoolNotMind,girlTeamWithSchoolNotMind)
match(boyTeamWithMyScool,girlTeamWithMySchool)
match(boyTeamWithOtherSchool,girlTeamWithOtherSchool)








