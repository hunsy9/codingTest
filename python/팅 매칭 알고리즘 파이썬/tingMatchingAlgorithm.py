import teamClass

teams = teamClass.AllTeamData()
def dataInitialize():
    teamDatas = open("match_test_case.txt", 'r')
    for teamData in teamDatas:
        e = list(map(str, teamData.split()))
        teamSchoolIndexList = list(map(int, e[2].split(",")))
        preferenceFilter = list(map(int, e[4].split(",")))
        teams.add(teamClass.Team(int(e[0]),int(e[1]),teamSchoolIndexList,int(e[3]),preferenceFilter,int(e[5])))
def matching(teams):
    for i in teams.AllTeamData: ##teams.AllTeamData로 매칭신청 중인 팀들이 모여있는 리스트 접근가능
        print(i.teamGender)
    # teams.printAllTeams() #teams.printAllTeams로 매칭신청 중인 팀들의 정보 출력 , 그냥 보기 편하게 출력할라고 만들어 놓음

dataInitialize()
matching(teams)






