<template>
  <div>
    <h4>Parameters</h4>
    <p>
      Here are all parameters you can use to control how your sprites will look
      like (v1)!
    </p>
    <ul>
      <li>
        <b>q:</b> query string, generates a unique sprite for any value (string)
      </li>
      <li>
        <b>n_iters:</b> controls the number of iterations to run the automata
        (integer)
      </li>
      <li>
        <b>extinction:</b> controls how many dead cells will stay dead (float,
        0-1)
      </li>
      <li>
        <b>survival:</b> controls how many live cells will stay alive (float,
        0-1)
      </li>
      <li><b>size:</b> size of the image, in pixels (integer)</li>
    </ul>
  </div>
</template>

<style scoped></style>
