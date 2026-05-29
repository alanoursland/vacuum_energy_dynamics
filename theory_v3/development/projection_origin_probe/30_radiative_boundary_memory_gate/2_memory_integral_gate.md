# Memory as integrated news

The script uses a compact pulse witness

```text
N(t)=A t (T-t),   0 <= t <= T.
```

It verifies that the news vanishes at the endpoints but has nonzero integrated memory:

```text
Delta C = ∫_0^T N(t) dt = A T^3/6.
```

So boundary memory is a permanent tensor displacement, not persistent news.
