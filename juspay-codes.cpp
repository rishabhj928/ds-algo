
The Nagging React newbie
#include<bits/stdc++.h>
using namespace std;
int main()
{
    unordered_map<int,vector<int>>mp;
    unordered_map<int,int>visit;
    int n,m,a,b;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a;
        mp[a]={};
    }
    cin>>m;
    for(int i=0;i<m;i++)
    {
        cin>>a>>b;
        mp[a].push_back(b);
    }
    cin>>a>>b;
    vector<int>ans;
    queue<int>q;
    visit[a]=1;
    q.push(a);
    while(!q.empty())
    {
        int y=q.front();
        q.pop();
        for(int i:mp[y])
        {
            if(visit[i]==0)
            {
                if(i==b)
                ans.push_back(y);
                else 
                {
                    visit[i]=1;
                    q.push(i);
                }
            }
        }
    }
    sort(ans.begin(),ans.end());
    for(int i:ans)
    cout<<i<<" ";
}


Learn JS
#include<bits/stdc++.h>
using namespace std;
vector<pair<long long int,long long int>> a[100000];
vector<bool> vis(100000,0);
long long int mn=999999999999999,ans=0,k=mn;
void dfs(long long int u,long long int v)
{
  if(u==v)
  {
    if(mn>ans)
    {
      mn=ans;
    }
  }
  vis[u]=1;
  for(auto j: a[u])
  {
    if(vis[j.first]==0)
    {
      ans+=j.second;
      vis[j.first]==1;
      dfs(j.first,v);
      vis[j.first]==0;
      ans-=j.second;
    }
  }
  vis[u]=0;
}
int main()
{
    long long int n,e,x,y,i,w;
    cin>>n;
    for(i=0;i<n;i++)
    {
     cin>>x;
    }
    cin>>e;
    for(i=0;i<e;i++)
    {
      cin>>x>>y>>w;
      a[x].push_back({y,w});
    }
    cin>>x>>y;
    dfs(x,y);
    if(mn==k)
    cout<<"-1";
    else
    cout<<mn;
}


Find Reachability
#include<bits/stdc++.h>
using namespace std;
vector<long long int> a[100000];
vector<long long int> vis(100000,0); 
void dfs(long long int s,long long int d)
{
  vis[s]=1;
  for(auto c:a[s])
  {
   if(vis[c]==0)
   {
    vis[c]=1;
    dfs(c,d);
   }
  }
}
int main() 
{
  long long int n,i,x,y,e;
  cin>>n;
  for(i=0;i<n;i++)
  {
  cin>>x;
  }
  cin>>e;
  for(i=0;i<e;i++)
  {
  cin>>x>>y;
  a[x].push_back(y);
  }
  cin>>x>>y;
  dfs(x,y);
  if(vis[x]==1 && vis[y]==1)
  cout<<"1\n";
  else
  cout<<"0\n";

}