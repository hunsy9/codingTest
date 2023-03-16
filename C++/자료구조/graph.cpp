#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
vector<pair<int, int>> meltIce;
vector<vector<int>> graph;
vector<vector<bool>> visited;

int n, m;
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

void bfs()
{
    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));
    visited[0][0] = true;

    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && ny >= 0 && nx < n && ny < m)
            {
                if (!graph[nx][ny] && !visited[nx][ny])
                {
                    q.push(make_pair(nx, ny));
                    visited[nx][ny] = 1;
                }
                else if (graph[nx][ny] && !visited[nx][ny])
                {
                    meltIce.push_back(make_pair(nx, ny));
                }
            }
        }
    }
}

int main(void)
{
    cin >> n >> m;
    graph.resize(n, vector<int>(m, 0));
    visited.resize(n, vector<bool>(m, false));
    for (int i = 0; i < n; i++)
    {
        string line;
        cin >> line;
        for (int j = 0; j < m; j++)
        {
            graph[i][j] = line[j] - '0';
        }
    }

    int year = 1;
    while (true)
    {

        bfs();
        for (int i = 0; i < meltIce.size(); i++)
        {
            int x = meltIce[i].first;
            int y = meltIce[i].second;
            graph[x][y] = 0;
        }

        int count = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (graph[i][j])
                {
                    count++;
                }
            }
        }

        if (count == 0)
        {
            cout << year << endl;
            break;
        }

        year++;

        fill(visited.begin(), visited.end(), vector<bool>(m, false));
        meltIce.clear();
    }

    return 0;
}
