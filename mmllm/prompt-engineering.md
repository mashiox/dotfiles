# Prompt Engineering

## Rowan's Perfect Prompt

Source: [Rowan Cheung 30 Oct 2023](https://twitter.com/rowancheung/status/1718985386267906265)

Key Takeaways: Including every tags in every prompt is not essential. Focusing on the more important tags should be the first priority.

<div class="container">
<p><span class="tag persona">[persona]</span> You are an individual who has adopted a healthier lifestyle over the past year, <span class="tag context">[context]</span> resulting in better physical and mental well-being. Inspired by your journey, a few friends have asked for advice on starting their own health journeys.</p>

<p><span class="tag task">[task]</span> Write a <span class="tag format">[format]</span> message <span class="tag context">[context]</span> to share in a group chat with interested friends.</p>
<p><span class="tag examples">[examples]</span> The message should outline the steps you took, share some challenges and how you overcame them, and offer to support them as they embark on their own journeys.</p>

<p><span class="tag tone">[tone]</span> Use motivational and empathetic language.</p>

Tag definitions in their order of importance:
| Tag | Description |
| --- | --- |
| <span class="tag task">[task]</span> | Clearly define your end goal |
| <span class="tag context">[context]</span> | Tailor your responses |
| <span class="tag examples">[examples]</span> | Examples will help shape the output style, structure, and tone |
| <span class="tag persona">[persona]</span> | Use a specific expertise set |
| <span class="tag format">[format]</span> | Bullet points, markdown, table, etc. |
| <span class="tag tone">[tone]</span> | Add layer of emotional context |

</div>

## Questions

These three key questions can help guide you in the right direction:

1. What's the user's background?
2. What does success look like?
3. What environment are they in?

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1, h2 {
  color: /* Header color from image */;
}

p {
  color: /* Paragraph text color from image */;
}

.tags {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.tag {
  background-color: /* Tag background color from image */;
  color: /* Tag text color from image */;
  padding: 5px 10px;
  border-radius: 5px;
}

.task {
    background-color: red;
}
.context {
    background-color: orange;
    color: black;
}
.examples {
    background-color: yellow;
    color: black;
}
.persona {
    background-color: green;
    color: black;
}
.format {
    background-color: blue;
}
.tone {
    background-color: purple;
}

.footer {
  text-align: center;
  color: /* Footer text color from image */;
  margin-top: 20px;
}

</style>