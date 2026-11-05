// All tight speed sets: n runners (n-1 moving speeds), max speed<=B. Exact arithmetic via a common
// denominator: t = a/D with D = 2*n*lcm-free approach: cell endpoints stored as fractions compared by cross-multiplication.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef long long ll;
typedef struct {ll p,q;} Fr;
static int cmp(const void*a,const void*b){const Fr*x=a,*y=b;__int128 l=(__int128)x->p*y->q,r=(__int128)y->p*x->q;return l<r?-1:(l>r?1:0);}
#define MAXW 2048
static int n,B,N,W; static uint64_t mask[400][MAXW]; static uint64_t full[MAXW];
static int *order; static int nres=0; static ll nodes=0;
static ll g(ll a,ll b){while(b){ll t=a%b;a=b;b=t;}return a<0?-a:a;}
static int chosen[32]; static char banned[400];
static int cov[60000][400]; static int ncov[60000];
static int cnt_cmp(const void*a,const void*b){return ncov[*(int*)a]-ncov[*(int*)b];}
static void go(uint64_t*cur,int d){
  nodes++;
  int cell=-1;
  for(int k=0;k<N;k++){int c=order[k]; if(!((cur[c>>6]>>(c&63))&1)){cell=c;break;}}
  if(cell<0){
    if(d==n-1){ll gg=0;for(int i=0;i<d;i++)gg=g(gg,chosen[i]);
      if(gg==1){int s[32];memcpy(s,chosen,sizeof(int)*d);
        for(int i=0;i<d;i++)for(int j=i+1;j<d;j++)if(s[j]<s[i]){int t=s[i];s[i]=s[j];s[j]=t;}
        printf("  (");for(int i=0;i<d;i++)printf("%d%s",s[i],i<d-1?",":"");printf(")\n");fflush(stdout);nres++;}
    } else {
      // smaller cover => pad not needed for tight sets under LRC; report
      printf("  SMALL COVER d=%d:",d);for(int i=0;i<d;i++)printf(" %d",chosen[i]);printf("\n");fflush(stdout);
    }
    return;
  }
  if(d==n-1) return;
  int banlist[400],nb=0;
  for(int i=0;i<ncov[cell];i++){int v=cov[cell][i];int dup=0;for(int j=0;j<d;j++)if(chosen[j]==v)dup=1;if(dup||banned[v])continue;
    uint64_t nx[MAXW];for(int w=0;w<W;w++)nx[w]=cur[w]|mask[v][w];
    chosen[d]=v;
    go(nx,d+1);
    banned[v]=1;banlist[nb++]=v;
  }
  for(int i=0;i<nb;i++)banned[banlist[i]]=0;
}
int main(int argc,char**argv){n=atoi(argv[1]);B=atoi(argv[2]);
  int cap=4*B*B+16;Fr*p=malloc(sizeof(Fr)*cap);int m=0;
  p[m++]=(Fr){0,1};p[m++]=(Fr){1,2};
  for(int v=1;v<=B;v++)for(int k=0;k<=v;k++)for(int s=-1;s<=1;s+=2){ll a=k*n+s,b=(ll)v*n; if(a>0&&2*a<b){ll gg=g(a,b);p[m++]=(Fr){a/gg,b/gg};}}
  qsort(p,m,sizeof(Fr),cmp);int u=0;for(int i=0;i<m;i++)if(u==0||cmp(&p[u-1],&p[i])!=0)p[u++]=p[i];m=u;
  N=m-1;W=(N+63)/64; if(N>=60000||W>MAXW){printf("too big N=%d\n",N);return 1;}
  for(int i=0;i<N;i++){ // midpoint a/b
    ll a=p[i].p*p[i+1].q+p[i+1].p*p[i].q,b=2*p[i].q*p[i+1].q;
    for(int v=1;v<=B;v++){ // ||v a/b|| <= 1/n  <=> n*dist(va mod b, b) <= b
      ll r=((__int128)v*a)%b; ll dd=r<b-r?r:b-r;
      if((__int128)n*dd<=b){mask[v][i>>6]|=1ULL<<(i&63);cov[i][ncov[i]++]=v;}
    }
  }
  order=malloc(sizeof(int)*N);for(int i=0;i<N;i++)order[i]=i;qsort(order,N,sizeof(int),cnt_cmp);
  printf("n=%d B=%d cells=%d\n",n,B,N);fflush(stdout);
  uint64_t cur[MAXW];memset(cur,0,sizeof(cur));go(cur,0);
  printf("done results(with repeats)=%d nodes=%lld\n",nres,nodes);return 0;}
