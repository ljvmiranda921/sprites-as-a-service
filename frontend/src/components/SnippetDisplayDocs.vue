<template>
  <div>
    <h4>Parameters</h4>
    <p>
      Control the appearance of your sprites using these parameters!
    </p>
    <div>
      <ul>
        <li>
          <b class="param">q:</b> query string, generates a unique sprite for
          any value (string)
        </li>
        <li>
          <b class="param">n_iters:</b> number of iterations to run the automata
          (integer)
        </li>
        <li>
          <b class="param">extinction:</b> controls how many dead cells will
          stay dead (float, 0-1)
        </li>
        <li>
          <b class="param">survival:</b> controls how many live cells will stay
          alive (float, 0-1)
        </li>
        <li>
          <b class="param">size:</b> size of the image, in pixels (integer)
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.param {
  color: #ffa300;
}
</style>
